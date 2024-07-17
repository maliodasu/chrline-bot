"""create_thrift_tables

Revision ID: 8f85466d5c50
Revises:
Create Date: 2024-03-17 11:09:21.580071

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8f85466d5c50'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('locations',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('address', sa.Text(), nullable=False),
    sa.Column('latitude', sa.Double(), nullable=False),
    sa.Column('longitude', sa.Double(), nullable=False),
    sa.Column('phone', sa.String(length=30), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('provider', sa.String(length=255), nullable=True),
    sa.Column('accuracy', sa.String(length=255), nullable=True),
    sa.Column('altitude_meters', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('messages',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('from', sa.String(length=50), nullable=False),
    sa.Column('to', sa.String(length=50), nullable=False),
    sa.Column('to_type', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.BigInteger(), nullable=False),
    sa.Column('delivered_time', sa.BigInteger(), nullable=True),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.Column('has_content', sa.Boolean(), nullable=True),
    sa.Column('content_type', sa.Integer(), nullable=True),
    sa.Column('content_preview', sa.LargeBinary(), nullable=True),
    sa.Column('content_metadata', sa.JSON(), nullable=False),
    sa.Column('session_id', sa.Integer(), nullable=True),
    sa.Column('message_id', sa.String(length=50), nullable=True),
    sa.Column('chunks', sa.JSON(), nullable=False),
    sa.Column('relation_message_id', sa.String(length=255), nullable=True),
    sa.Column('message_relation_type', sa.Integer(), nullable=True),
    sa.Column('read_count', sa.Integer(), nullable=True),
    sa.Column('related_message_service_code', sa.Integer(), nullable=True),
    sa.Column('reactions', sa.JSON(), nullable=False),
    sa.Column('op_type', sa.Integer(), nullable=True),
    sa.Column('is_e2ee', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['locations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('operations',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('revision', sa.Integer(), nullable=False),
    sa.Column('created_time', sa.BigInteger(), nullable=False),
    sa.Column('type', sa.Integer(), nullable=False),
    sa.Column('type_name', sa.String(length=255), nullable=True),
    sa.Column('req_seq', sa.Integer(), nullable=False),
    sa.Column('checksum', sa.Integer(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('param1', sa.String(length=255), nullable=True),
    sa.Column('param2', sa.String(length=255), nullable=True),
    sa.Column('param3', sa.String(length=255), nullable=True),
    sa.Column('message_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['message_id'], ['messages.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('operations')
    op.drop_table('messages')
    op.drop_table('locations')
    # ### end Alembic commands ###
